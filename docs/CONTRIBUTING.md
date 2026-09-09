# Инструкции по добавлению фотографий

## Требования к фотографиям

- **Разрешение**: минимум 2000x1500 пикселей
- **Формат**: JPG, PNG или WebP
- **Размер файла**: не более 5 МБ (для оригинала)
- **Качество**: высокое разрешение, хорошая освещенность

## Процесс добавления

### Шаг 1: Подготовка файлов

1. Возьмите оригинальную фотографию
2. Убедитесь, что она соответствует требованиям выше
3. Создайте миниатюру размером 300x300px (сохраните как `_thumb.jpg`)

**Пример:**
```bash
# Если у вас есть ImageMagick
convert photo.jpg -resize 300x300 photo_thumb.jpg
```

### Шаг 2: Поместите файлы

```
photos/
  ├── originals/
  │   └── hospital_name_001.jpg
  └── thumbnails/
      └── hospital_name_001_thumb.jpg
```

### Шаг 3: Обновите каталог

Добавьте запись в `metadata/catalog.json`:

```json
{
  "id": "unique_id_001",
  "title": "Name of Hospital",
  "location": {
    "country": "Country",
    "region": "Region",
    "city": "City"
  },
  "year_closed": 2020,
  "year_built": 1950,
  "filename": "hospital_name_001.jpg",
  "thumbnail": "hospital_name_001_thumb.jpg",
  "description": "Detailed description of what is shown in the photo",
  "photographer": "Your Name",
  "date_taken": "2023-01-15",
  "image_info": {
    "width": 3000,
    "height": 2000,
    "file_size_kb": 2048,
    "format": "jpg"
  },
  "tags": ["building", "interior", "windows"],
  "license": "CC BY-NC-SA 4.0",
  "source_url": ""
}
```

## Поля метаданных

| Поле | Описание | Обязательное |
|------|---------|-----------|
| id | Уникальный идентификатор (формат: hospital_code_NNN) | ✓ |
| title | Название больницы | ✓ |
| location | Местоположение (страна, регион, город) | ✓ |
| year_closed | Год закрытия | ✓ |
| year_built | Год постройки | ✓ |
| filename | Имя файла оригинала | ✓ |
| thumbnail | Имя файла миниатюры | ✓ |
| description | Описание фотографии (50-500 символов) | ✓ |
| photographer | Имя фотографа или "Anonymous" | ✓ |
| date_taken | Дата съемки (YYYY-MM-DD) | ✓ |
| image_info | Информация об изображении | ✓ |
| tags | Массив тегов для категоризации | ✓ |
| license | Лицензия использования | ✓ |
| source_url | URL источника (если применимо) | - |

## Рекомендуемые лицензии

- CC0 (общественное достояние)
- CC BY 4.0 (Атрибуция)
- CC BY-SA 4.0 (Атрибуция - Sharealike)
- CC BY-NC 4.0 (Атрибуция - Некоммерческое)
- CC BY-NC-SA 4.0 (Атрибуция - Некоммерческое - Sharealike)

## Примеры тегов

- building, interior, exterior
- windows, doors, hallway, room
- damage, decay, overgrown
- furniture, equipment, medical
- architecture, modern, historical

## Проверка качества

Перед добавлением убедитесь что:
- [ ] Изображение четкое и хорошо освещено
- [ ] Фотография показывает заброшенную больницу
- [ ] Метаданные заполнены полностью
- [ ] Лицензия указана корректно
- [ ] Размер файла соответствует требованиям

## Вопросы?

Смотрите основной README.md для получения дополнительной информации.
