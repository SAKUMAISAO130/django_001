環境構築手順

■　ディレクトリ作成
mkdir django_001
cd django_001


■　仮想環境　初期化
python3 -m venv myvenv


■　仮想環境　起動
source myvenv/bin/activate


■　pip　更新
python -m pip install --upgrade pip


■　パッケージ一覧更新
djangogirls/ フォルダ内に requirements.txt という名前で保存してください。
vim requirements.txt


■　requirements.txt　に記載
Django~=2.2.4


■　パッケージインストール
pip install -r requirements.txt


■　プロジェクト作成
django-admin startproject mysite .


■　設定　変更
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


■　DB　構築
python manage.py migrate


■　サーバー起動
python manage.py runserver


■　ブラウザ表示
http://127.0.0.1:8000/


■　git　初期化
git init


■　gitignore
vim .gitignore


■　gitignore　中身
*.pyc
*~
/.vscode
__pycache__
myvenv
db.sqlite3
/static
.DS_Store


