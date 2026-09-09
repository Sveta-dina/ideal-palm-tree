#!/usr/bin/env python3
"""
Utility script to manage and validate the abandoned psychiatric hospital photos archive.
"""

import json
import os
from pathlib import Path
from datetime import datetime
import sys


class PhotoArchive:
    def __init__(self, catalog_path="metadata/catalog.json"):
        self.catalog_path = catalog_path
        self.photos_dir = Path("photos")
        self.catalog = self._load_catalog()

    def _load_catalog(self):
        """Load the catalog from JSON file."""
        if not Path(self.catalog_path).exists():
            return {"version": "1.0", "last_updated": "", "total_photos": 0, "photos": []}

        with open(self.catalog_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save_catalog(self):
        """Save the catalog to JSON file."""
        self.catalog['last_updated'] = datetime.now().isoformat()
        self.catalog['total_photos'] = len(self.catalog['photos'])

        with open(self.catalog_path, 'w', encoding='utf-8') as f:
            json.dump(self.catalog, f, ensure_ascii=False, indent=2)

    def validate_photo(self, photo_entry):
        """Validate a photo entry."""
        required_fields = [
            'id', 'title', 'location', 'year_closed', 'year_built',
            'filename', 'thumbnail', 'description', 'photographer',
            'date_taken', 'image_info', 'tags', 'license'
        ]

        errors = []
        for field in required_fields:
            if field not in photo_entry:
                errors.append(f"Missing required field: {field}")

        # Check if files exist
        original_path = self.photos_dir / 'originals' / photo_entry.get('filename', '')
        thumbnail_path = self.photos_dir / 'thumbnails' / photo_entry.get('thumbnail', '')

        if not original_path.exists():
            errors.append(f"Original file not found: {original_path}")
        if not thumbnail_path.exists():
            errors.append(f"Thumbnail file not found: {thumbnail_path}")

        return errors

    def add_photo(self, photo_data):
        """Add a new photo to the catalog."""
        errors = self.validate_photo(photo_data)
        if errors:
            print(f"Validation errors for {photo_data.get('id', 'unknown')}:")
            for error in errors:
                print(f"  - {error}")
            return False

        # Check if ID already exists
        existing_ids = [p['id'] for p in self.catalog['photos']]
        if photo_data['id'] in existing_ids:
            print(f"Error: Photo with ID '{photo_data['id']}' already exists")
            return False

        self.catalog['photos'].append(photo_data)
        self.save_catalog()
        print(f"Successfully added photo: {photo_data['id']}")
        return True

    def list_photos(self):
        """List all photos in the catalog."""
        if not self.catalog['photos']:
            print("No photos in the catalog yet.")
            return

        print("\n" + "="*80)
        print(f"Total photos: {len(self.catalog['photos'])}")
        print("="*80)

        for photo in self.catalog['photos']:
            print(f"\nID: {photo['id']}")
            print(f"Title: {photo['title']}")
            print(f"Location: {photo['location']['city']}, {photo['location']['region']}, {photo['location']['country']}")
            print(f"Year Closed: {photo['year_closed']}")
            print(f"Photographer: {photo['photographer']}")
            print(f"License: {photo['license']}")

    def validate_all(self):
        """Validate all photos in the catalog."""
        if not self.catalog['photos']:
            print("No photos to validate.")
            return True

        all_valid = True
        for photo in self.catalog['photos']:
            errors = self.validate_photo(photo)
            if errors:
                print(f"\nErrors in photo '{photo['id']}':")
                for error in errors:
                    print(f"  - {error}")
                all_valid = False

        if all_valid:
            print("✓ All photos validated successfully!")
        return all_valid

    def get_statistics(self):
        """Get statistics about the archive."""
        if not self.catalog['photos']:
            print("No photos in the catalog yet.")
            return

        locations = {}
        years = {}

        for photo in self.catalog['photos']:
            country = photo['location']['country']
            locations[country] = locations.get(country, 0) + 1

            year = photo['year_closed']
            years[year] = years.get(year, 0) + 1

        print("\n" + "="*80)
        print("ARCHIVE STATISTICS")
        print("="*80)
        print(f"Total photos: {len(self.catalog['photos'])}")

        print(f"\nPhotos by country:")
        for country, count in sorted(locations.items()):
            print(f"  {country}: {count}")

        print(f"\nPhotos by closing year:")
        for year, count in sorted(years.items()):
            print(f"  {year}: {count}")


def main():
    archive = PhotoArchive()

    if len(sys.argv) < 2:
        print("Usage: python manage_photos.py <command> [args]")
        print("\nCommands:")
        print("  list              - List all photos")
        print("  validate          - Validate all photos")
        print("  stats             - Show archive statistics")
        return

    command = sys.argv[1]

    if command == 'list':
        archive.list_photos()
    elif command == 'validate':
        archive.validate_all()
    elif command == 'stats':
        archive.get_statistics()
    else:
        print(f"Unknown command: {command}")


if __name__ == '__main__':
    main()
