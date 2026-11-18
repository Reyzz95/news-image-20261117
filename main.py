#!/usr/bin/env python3
# This program is deterministic because it performs a straightforward, fixed byte-for-byte
# copy of a static source asset (entry.png) to a destination directory without relying
# on random number generators, timestamps, network requests, or dynamic state.
import os
import sys
import shutil

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(script_dir, 'entry.png')  # Four-panel editorial collage summarizing the biggest world news of 17 November 2026 (NVIDIA Q3 results, Crimea Bridge strike, Hormuz tanker attack, and the upcoming Xi-Trump-Putin summit)
    
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    
    dst = os.path.join(output_dir, 'entry.png')
    
    if not os.path.exists(src):
        print(f"Error: Source file {src} does not exist.", file=sys.stderr)
        sys.exit(1)
        
    shutil.copy2(src, dst)
    
    src_size = os.path.getsize(src)
    dst_size = os.path.getsize(dst)
    
    if src_size != dst_size:
        print(f"Error: Size mismatch! Source size ({src_size}) != Destination size ({dst_size})", file=sys.stderr)
        sys.exit(1)
        
    print(f"Successfully copied {src} to {dst} ({dst_size} bytes).")

if __name__ == '__main__':
    main()
