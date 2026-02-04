import os
import shutil

def organize(src_root, dest_root, limit_per_class=1000):
    # Map the Kaggle subfolders to our binary classes
    # Kaggle structure: train/freshapples, train/rottenapples, etc.
    
    splits = ["train", "test"]
    for split in splits:
        # The dataset might be nested under 'dataset' or directly
        src_split = os.path.join(src_root, "dataset", split)
        if not os.path.exists(src_split):
            src_split = os.path.join(src_root, split)
        
        if not os.path.exists(src_split):
            print(f"Split {split} not found in {src_root}")
            continue
            
        dest_split = os.path.join(dest_root, split if split == "train" else "validation")
        
        os.makedirs(os.path.join(dest_split, "fresh"), exist_ok=True)
        os.makedirs(os.path.join(dest_split, "rotten"), exist_ok=True)
        
        for folder in os.listdir(src_split):
            src_folder_path = os.path.join(src_split, folder)
            if not os.path.isdir(src_folder_path):
                continue
                
            if "fresh" in folder.lower():
                target_class = "fresh"
            elif "rotten" in folder.lower():
                target_class = "rotten"
            else:
                continue
                
            print(f"Moving files from {folder} to {target_class} (limit {limit_per_class})...")
            count = 0
            for img in os.listdir(src_folder_path):
                if count >= limit_per_class:
                    break
                shutil.copy(os.path.join(src_folder_path, img), os.path.join(dest_split, target_class, f"{folder}_{img}"))
                count += 1

if __name__ == "__main__":
    pass
