# 概要

Nginx + MySQLをDjangoで利用するためのDocker環境です。

## 環境設定

- .env
  - 環境変数を指定してください。
    - MODE
      - localがローカル
      - productionが本番
- command
  - コマンド関連を保存します。
- environment
  - 環境ファイルを保存します。

## 必須事項

Httpsの対応が必要。
letsencryptで生成したファイルをnginxコンテナにマウントしているので、それらのファイルを用意すること。