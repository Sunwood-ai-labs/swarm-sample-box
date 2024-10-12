import sqlite3

# グローバル接続
conn = None


def get_connection():
    """データベース接続を取得する関数"""
    global conn
    if conn is None:
        conn = sqlite3.connect("application.db")
    return conn


def create_database():
    """データベースとテーブルを作成する関数"""
    # SQLiteデータベースに接続
    conn = get_connection()
    cursor = conn.cursor()

    # Usersテーブルの作成
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            first_name TEXT,
            last_name TEXT,
            email TEXT UNIQUE,
            phone TEXT
        )
    """
    )

    # PurchaseHistoryテーブルの作成
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS PurchaseHistory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            date_of_purchase TEXT,
            item_id INTEGER,
            amount REAL,
            FOREIGN KEY (user_id) REFERENCES Users(user_id)
        )
    """
    )

    # Productsテーブルの作成
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Products (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            price REAL NOT NULL
        );
        """
    )

    # 変更を保存（コミット）
    conn.commit()


def add_user(user_id, first_name, last_name, email, phone):
    """ユーザーを追加する関数"""
    conn = get_connection()
    cursor = conn.cursor()

    # ユーザーが既に存在するかチェック
    cursor.execute("SELECT * FROM Users WHERE user_id = ?", (user_id,))
    if cursor.fetchone():
        return

    try:
        cursor.execute(
            """
            INSERT INTO Users (user_id, first_name, last_name, email, phone)
            VALUES (?, ?, ?, ?, ?)
        """,
            (user_id, first_name, last_name, email, phone),
        )

        conn.commit()
    except sqlite3.Error as e:
        print(f"データベースエラー: {e}")


def add_purchase(user_id, date_of_purchase, item_id, amount):
    """購入履歴を追加する関数"""
    conn = get_connection()
    cursor = conn.cursor()

    # 購入履歴が既に存在するかチェック
    cursor.execute(
        """
        SELECT * FROM PurchaseHistory
        WHERE user_id = ? AND item_id = ? AND date_of_purchase = ?
    """,
        (user_id, item_id, date_of_purchase),
    )
    if cursor.fetchone():
        return

    try:
        cursor.execute(
            """
            INSERT INTO PurchaseHistory (user_id, date_of_purchase, item_id, amount)
            VALUES (?, ?, ?, ?)
        """,
            (user_id, date_of_purchase, item_id, amount),
        )

        conn.commit()
    except sqlite3.Error as e:
        print(f"データベースエラー: {e}")


def add_product(product_id, product_name, price):
    """製品を追加する関数"""
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
        INSERT INTO Products (product_id, product_name, price)
        VALUES (?, ?, ?);
        """,
            (product_id, product_name, price),
        )

        conn.commit()
    except sqlite3.Error as e:
        print(f"データベースエラー: {e}")


def close_connection():
    """データベース接続を閉じる関数"""
    global conn
    if conn:
        conn.close()
        conn = None


def preview_table(table_name):
    """テーブルの内容をプレビューする関数"""
    conn = sqlite3.connect("application.db")
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")  # 最初の5行に制限

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


def initialize_database():
    """データベースを初期化し、サンプルデータを追加する関数"""
    global conn

    # データベーステーブルの初期化
    create_database()

    # 初期ユーザーの追加
    initial_users = [
        (1, "Alice", "Smith", "alice@test.com", "123-456-7890"),
        (2, "Bob", "Johnson", "bob@test.com", "234-567-8901"),
        (3, "Sarah", "Brown", "sarah@test.com", "555-567-8901"),
        # 必要に応じて初期ユーザーを追加
    ]

    for user in initial_users:
        add_user(*user)

    # 初期購入履歴の追加
    initial_purchases = [
        (1, "2024-01-01", 101, 99.99),
        (2, "2023-12-25", 100, 39.99),
        (3, "2023-11-14", 307, 49.99),
    ]

    for purchase in initial_purchases:
        add_purchase(*purchase)

    # 初期製品の追加
    initial_products = [
        (7, "帽子", 19.99),
        (8, "ウールソックス", 29.99),
        (9, "靴", 39.99),
    ]

    for product in initial_products:
        add_product(*product)
