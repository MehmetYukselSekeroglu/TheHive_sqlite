CREATE TABLE IF NOT EXISTS "system_core" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    unique_key VARCHAR(100) NOT NULL UNIQUE,
    value VARCHAR(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS "blob_storage" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    unique_blob_key TEXT NOT NULL UNIQUE,
    key_value BYTEA NOT NULL,
    data_type TEXT NOT NULL DEFAULT 'user',
    information_notes TEXT DEFAULT NULL
);
CREATE TABLE IF NOT EXISTS "authentication" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(128) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL
);
CREATE TABLE IF NOT EXISTS "face_recognition_standart" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    face_picture_blob BLOB NOT NULL, 
    picture_sha1_hash BLOB NOT NULL UNIQUE,
    face_embedding_data BLOB NOT NULL,
    landmarks_2d BLOB NOT NULL,
    face_box BLOB NOT NULL,
    face_name TEXT NOT NULL,
    add_date TIMESTAMP DEFAULT NOW()
);
