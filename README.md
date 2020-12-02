環境構築手順

【作業】　ディレクトリ作成
mkdir django_001
cd django_001


【作業】　仮想環境　初期化
python3 -m venv myvenv


【作業】　仮想環境　起動
source myvenv/bin/activate


【作業】　pip　更新
python -m pip install --upgrade pip


【作業】　パッケージ一覧更新
djangogirls/ フォルダ内に requirements.txt という名前で保存してください。
vim requirements.txt


【作業】　requirements.txt　に記載
Django~=2.2.4


【作業】　パッケージインストール
pip install -r requirements.txt


【作業】　プロジェクト作成
django-admin startproject mysite .


【作業】　設定　変更
--------
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
--------
LANGUAGE_CODE = 'ja'
--------
TIME_ZONE = 'Asia/Tokyo'
--------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
--------


【作業】　DB　構築
python manage.py migrate


【作業】　サーバー起動
python manage.py runserver


【作業】　ブラウザ表示
http://127.0.0.1:8000/


【作業】　git　初期化
git init


【作業】　gitignore
vim .gitignore


【作業】　gitignore　中身
*.pyc
*~
/.vscode
__pycache__
myvenv
db.sqlite3
/static
.DS_Store


【作業】　pythonanywhere　を最新化する
pip3.6 install --user pythonanywhere

【作業】　GIT pull　してデプロイ
pa_autoconfigure_django.py --python=3.6 https://github.com/<your-github-username>/my-first-blog.git













