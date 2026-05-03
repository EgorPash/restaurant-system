import subprocess
import sys
import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Запускает FastAPI-сервер на порту 8001'

    def handle(self, *args, **options):
        fastapi_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'fastapi_app')
        cmd = ['uvicorn', 'main:app', '--host', '0.0.0.0', '--port', '8001', '--reload']

        self.stdout.write('Запуск FastAPI на порту 8001...')
        subprocess.call(cmd, cwd=fastapi_dir)