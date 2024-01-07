#!/bin/bash

echo $1

echo "OCR処理を実行中..."

python ./ocr.py $1 > output.txt

# スクリプト終了
echo "OCR処理が完了しました。"
