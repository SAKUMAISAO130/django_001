環境構築手順

1.　ディレクトリ作成
mkdir django_001
cd django_001


1.　仮想環境　初期化
python3 -m venv myvenv


1.　仮想環境　起動
source myvenv/bin/activate


1.　pip　更新
python -m pip install --upgrade pip


1.　パッケージ一覧更新
djangogirls/ フォルダ内に requirements.txt という名前で保存してください。
vim requirements.txt


1.　requirements.txt　に記載
Django~=2.2.4


1.　パッケージインストール
pip install -r requirements.txt


1.　プロジェクト作成
django-admin startproject mysite .


1.　設定　変更
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


1.　DB　構築
python manage.py migrate


1.　サーバー起動
python manage.py runserver


1.　ブラウザ表示
http://127.0.0.1:8000/


1.　git　初期化
git init


1.　gitignore
vim .gitignore


1.　gitignore　中身
*.pyc
*~
/.vscode
__pycache__
myvenv
db.sqlite3
/static
.DS_Store


1.　pythonanywhere　を最新化する
pip3.6 install --user pythonanywhere

1.　GIT pull　してデプロイ
pa_autoconfigure_django.py --python=3.6 https://github.com/<your-github-username>/my-first-blog.git













