import os
import json
import csv
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from tqdm import tqdm


try:
    import pillow_heif
    pillow_heif.register_heif_opener()
except ImportError:
    pass  


try:
    from pymediainfo import MediaInfo
except ImportError:
    MediaInfo = None
    print("⚠️ pymediainfo modülü eksik. Medya dosyaları işlenemez.")

def convert_to_serializable(value):
    if isinstance(value, tuple) and len(value) == 2:
        return float(value[0]) / float(value[1]) if value[1] != 0 else 0.0
    elif isinstance(value, list):
        return [convert_to_serializable(item) for item in value]
    elif isinstance(value, dict):
        return {k: convert_to_serializable(v) for k, v in value.items()}
    elif isinstance(value, (int, float, str, bool)) or value is None:
        return value
    return str(value)

def extract_exif(img):
    exif_data = img._getexif()
    if not exif_data:
        return {}
    meta = {}
    for tag_id, value in exif_data.items():
        tag = TAGS.get(tag_id, str(tag_id))
        if tag == "GPSInfo":
            gps_info = {}
            for t, v in value.items():
                sub_tag = GPSTAGS.get(t, str(t))
                gps_info[sub_tag] = convert_to_serializable(v)
            meta["GPSInfo"] = gps_info
        else:
            meta[tag] = convert_to_serializable(value)
    return meta

def get_gps_link(gps_info):
    try:
        def _convert(coord, ref):
            deg = float(coord[0])
            min = float(coord[1]) / 60.0
            sec = float(coord[2]) / 3600.0
            result = deg + min + sec
            if ref in ['S', 'W']:
                result *= -1
            return result
        lat = _convert(gps_info['GPSLatitude'], gps_info['GPSLatitudeRef'])
        lon = _convert(gps_info['GPSLongitude'], gps_info['GPSLongitudeRef'])
        return f"https://maps.google.com/?q={lat},{lon}"
    except Exception as e:
        return f"GPS link creation failed: {str(e)}"

def extract_mediainfo(file_path):
    if MediaInfo is None:
        return {"file": file_path, "error": "pymediainfo not installed"}
    try:
        media_info = MediaInfo.parse(file_path)
        data = {}
        for track in media_info.tracks:
            track_type = track.track_type
            for key, value in track.to_data().items():
                if value:
                    data[f"{track_type}_{key}"] = value
        return data
    except Exception as e:
        print(f"❌ Error reading media info from {file_path}: {e}")
        return {"file": file_path, "error": str(e)}

def extract_metadata(file_path):
    metadata = {"file": file_path}
    _, ext = os.path.splitext(file_path.lower())
    try:
        if ext in [".jpg", ".jpeg", ".tiff", ".tif", ".png", ".webp", ".heic", ".jfif", ".bmp"]:
            img = Image.open(file_path)
            exif = extract_exif(img)
            metadata.update(exif)
            if "GPSInfo" in exif:
                link = get_gps_link(exif["GPSInfo"])
                metadata["GoogleMaps"] = link

        elif ext in [".mp4", ".mov", ".avi", ".mkv", ".mp3", ".wav", ".3gp"]:
            media_meta = extract_mediainfo(file_path)
            metadata.update(media_meta)

        else:
            return None  
    except Exception as e:
        metadata["error"] = str(e)
        print(f"❌ Error processing {file_path}: {str(e)}")
    return metadata

def save_to_csv(metadata_list, output_file):
    if not metadata_list:
        return
    keys = set()
    for meta in metadata_list:
        keys.update(str(k) for k in meta.keys())
    keys = sorted(keys)
    with open(output_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for meta in metadata_list:
            writer.writerow({k: str(v) for k, v in meta.items()})

def save_to_txt(metadata_list, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for meta in metadata_list:
            f.write(f"File: {meta['file']}\n")
            for key, value in meta.items():
                if key != "file":
                    f.write(f"{key}: {value}\n")
            f.write("\n")

def main():
    path_input = input("\U0001F4C2 Enter the folder or file path to analyze metadata: ").strip()
    path = Path(os.path.normpath(path_input))

    if not path.exists():
        print(f"❌ Invalid path: {path_input}")
        return

    all_metadata = []

    if path.is_file():
        print(f"🔍 Processing file: {path}")
        meta = extract_metadata(str(path))
        if meta:
            all_metadata.append(meta)
    else:
        files = list(path.rglob("*"))
        if not files:
            print("⚠️ No files found in the specified folder.")
            return

        for file in tqdm(files, desc="Processing files"):
            if file.is_file():
                meta = extract_metadata(str(file))
                if meta:
                    all_metadata.append(meta)

    if not all_metadata:
        print("⚠️ No supported files found.")
        return

    json_output = "metadata_output.json"
    with open(json_output, "w", encoding="utf-8") as f:
        json.dump(all_metadata, f, indent=4, ensure_ascii=False)
    print(f"\n✅ Saved JSON output to: {json_output}")

    csv_output = "metadata_output.csv"
    save_to_csv(all_metadata, csv_output)
    print(f"✅ Saved CSV output to: {csv_output}")

    txt_output = "metadata_output.txt"
    save_to_txt(all_metadata, txt_output)
    print(f"✅ Saved TXT output to: {txt_output}")

    gps_files = [meta for meta in all_metadata if "GoogleMaps" in meta and not meta["GoogleMaps"].startswith("GPS link creation failed")]
    if gps_files:
        with open("gps_links.txt", "w", encoding="utf-8") as f:
            for meta in gps_files:
                f.write(f"{meta['file']}: {meta['GoogleMaps']}\n")
        print(f"✅ Saved GPS links to: gps_links.txt")
    else:
        print("ℹ️ No files with valid GPS data found.")

    print(f"📊 Total files analyzed: {len(all_metadata)}")

if __name__ == "__main__":
    main()
