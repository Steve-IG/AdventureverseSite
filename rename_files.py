import os

# Dictionary mapping old names to new names
file_mapping = {
    'Adventureverse+Create+Characters': 'create-characters.jpg',
    'Adventureverse+Create+Skills': 'create-skills.jpg',
    'Adventureverse+Create+Campaigns': 'create-campaigns.jpg',
    'Adventureverse+Share': 'share-creations.jpg',
    'Adventureverse+Play': 'play.jpg',
    'Imagination+Games+Logo': 'imagination-games-logo.png',
    'ADV+Logo+White.png': 'hero-bg.jpg'
}

# Change to assets directory
os.chdir('assets')

# Rename files
for old_name, new_name in file_mapping.items():
    try:
        if os.path.exists(old_name):
            os.rename(old_name, new_name)
            print(f"Successfully renamed {old_name} to {new_name}")
    except Exception as e:
        print(f"Error renaming {old_name}: {str(e)}")

print("Renaming complete!") 