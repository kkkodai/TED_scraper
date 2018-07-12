# TED_scraper
### videoをスクレイピング
- video_crawler.py
    -  クローリングにより取得したurlをcsvとして保存
    - total_page = 77 というのは20180423時点のもの、最新は[https://www.ted.com/talks?page=](https://www.ted.com/talks?page=)の最大番号をサイト右下からチェック可能
- video_scpaper.py
    - url先の動画を取得
    - 取ってこないことがあるため、ちゃんと動画が取れているか確認する必要あり(原因不明)
        - unscraped_df[link][count1].txtは取得できなかった動画のdf["link"][count1]が記載される

### csvデータ
- ted-link_video.csvは20180423時点のもの