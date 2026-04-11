from src.transform import clean_story

def test_clean_story():
    """Test that the transformation logic properly formats a raw API response."""
    raw_data = {
        "id": 12345,
        "title": "Test Title",
        "url": "http://example.com",
        "score": 100,
        "by": "test_user",
        "descendants": 50, # Should be ignored
        "type": "story"    # Should be ignored
    }
    
    cleaned = clean_story(raw_data)
    
    assert cleaned["id"] == 12345
    assert cleaned["title"] == "Test Title"
    assert cleaned["url"] == "http://example.com"
    assert cleaned["score"] == 100
    assert cleaned["author"] == "test_user"
    assert "retrieved_at" in cleaned
    assert "descendants" not in cleaned

def test_clean_story_missing_fields():
    """Test transformation logic with missing fields."""
    raw_data = {"id": 999}
    
    cleaned = clean_story(raw_data)
    
    assert cleaned["title"] == "No Title"
    assert cleaned["score"] == 0
    assert cleaned["author"] == "Unknown"
