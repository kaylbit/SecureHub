from flask import Flask, Blueprint, request, jsonify

SECRET_KEY = "Be_A_Good_HACKER"
DATABASE = "securehub.db"
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTE = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7
UPLOAD_FOLDER = "uploads"
MAX_UPLOAD_SIZE = 5 * 1024 * 1024
