#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil

def collect_dot_files(base_dir="dot_output", target_dir="start", line_count=118):
    # 确保目标文件夹存在
    os.makedirs(target_dir, exist_ok=True)

    # 遍历 dot_output 下所有子目录
    for root, dirs, files in os.walk(base_dir):
        for fname in files:
            if fname.endswith(".dot"):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath, "r") as f:
                        lines = f.readlines()
                    if len(lines) == line_count:
                        # 剪切到 start 文件夹
                        shutil.move(fpath, os.path.join(target_dir, fname))
                        print(f"✂️ Moved: {fpath} -> {target_dir}")
                except Exception as e:
                    print(f"⚠️ Error reading {fpath}: {e}")

if __name__ == "__main__":
    collect_dot_files()
