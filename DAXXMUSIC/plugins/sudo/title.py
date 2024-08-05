from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Define the '/br' command handler
@Client.on_message(filters.command("br"))
async def br_command_handler(client, message):
    # Check if the command has arguments
    if len(message.command) < 2:
        await message.reply_text("Please provide an image URL and caption after the command.")
        return

    # Extract image URL and caption from the command arguments
    image_url = message.command[1]
    caption = " ".join(message.command[2:])

    # Create inline keyboard with three buttons
    inline_keyboard = [
        [InlineKeyboardButton("Button 1", callback_data="button1_data")],
        [InlineKeyboardButton("Button 2", callback_data="button2_data")],
        [InlineKeyboardButton("Button 3", callback_data="button3_data")]
    ]
    reply_markup = InlineKeyboardMarkup(inline_keyboard)

    try:
        # Send the image with caption and inline keyboard
        await client.send_photo(
            chat_id=message.chat.id,
            photo=image_url,
            caption=caption,
            reply_markup=reply_markup
        )
    except Exception as e:
        print(e)
        await message.reply_text("Error: Failed to process the image URL.")
