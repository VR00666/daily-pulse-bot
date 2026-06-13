import requests
from datetime import datetime

def get_weather(city: str = "Thiruvananthapuram") -> str:
    """
    Fetches the live weather information for a specified city using wttr.in.
    
    Args:
        city (str): The name of the city. Defaults to "Thiruvananthapuram".
        
    Returns:
        str: A string representing the current weather.
    """
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        return f"Weather unavailable ({e})"

def get_quote() -> str:
    """
    Fetches a random motivational quote from the zenquotes.io API.
    
    Returns:
        str: A formatted string containing the quote and the author.
    """
    try:
        url = "https://zenquotes.io/api/random"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            quote = data[0].get("q", "Keep moving forward.")
            author = data[0].get("a", "Unknown")
            return f'"{quote}"\n— {author}'
        raise ValueError("Invalid response format")
    except Exception:
        return '"Keep moving forward."\n— Unknown'

def build_summary() -> str:
    """
    Generates the formatted daily summary containing date, weather, and a quote.
    
    Returns:
        str: The complete formatted daily summary.
    """
    date_str = datetime.now().strftime("%Y-%m-%d")
    weather = get_weather()
    quote = get_quote()
    
    summary = (
        "=================================\n"
        "PULSE DAILY SUMMARY\n"
        "=================================\n\n"
        "Date:\n"
        f"{date_str}\n\n"
        "Weather:\n"
        f"{weather}\n\n"
        "Quote:\n"
        f"{quote}"
    )
    return summary

def save_summary(summary: str) -> None:
    """
    Saves the generated summary to daily_summary.txt.
    
    Args:
        summary (str): The summary text to save.
    """
    with open("daily_summary.txt", "w", encoding="utf-8") as file:
        file.write(summary)

def run() -> None:
    """
    Main workflow function to generate, save, and display the daily summary.
    """
    import sys
    if sys.stdout.encoding.lower() != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
        
    summary = build_summary()
    save_summary(summary)
    print(summary)

if __name__ == "__main__":
    run()
