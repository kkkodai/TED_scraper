# TED_scraper
### videoをスクレイピング
- video_crawler.py
    -  クローリングにより取得したurlをcsvとして保存
    - total_page = 77 というのは20180423時点のもの、最新は[https://www.ted.com/talks?page=](https://www.ted.com/talks?page=)の最大番号をサイト右下からチェック可能
- video_scraper.py
    - url先の動画を取得
    - 取ってこないことがあるため、正しく取れているか確認する必要あり(原因不明)
        - unscraped_df[link][count1].txtは取得できなかった動画のdf["link"][count1]が記載される

### transcriptをスクレイピング
- script_scraper.py
    - 日英の字幕文を獲得(タグ付き)
    - 取ってこないことがあるため、正しく取れているか確認する必要あり(原因不明)
        - notexist_numberを確認

### コーパス作成
- script_regex.py
    - スクリプトの修正

- make_corpus.py
    - script_regex.pyにより作成されたファイルから日英コーパスを作成

### データセット
- ted-link.csvを使って作成
    - csv自体は20180423時点のもの
- ted_script
    - ted_script_tag_ja.zipはscript_scraper.pyから取得した日本語訳文のデータ
    - ted_script_tag_en.zipはscript_scraper.pyから取得した英語訳文のデータ
    - _抽出失敗したファイルもあり全部は取れていない_