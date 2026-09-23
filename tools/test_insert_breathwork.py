import pytest
from insert_breathwork import inject_breathwork, target_text, new_section

def test_inject_breathwork_happy_path():
    # Setup
    initial_content = f"<html><body><p>Before text</p>{target_text}<p>After text</p></body></html>"

    # Execute
    result = inject_breathwork(initial_content)

    # Verify
    # The new section should be inserted just before the target text
    expected_content = f"<html><body><p>Before text</p>{new_section}{target_text}<p>After text</p></body></html>"
    assert result == expected_content
    assert new_section in result

def test_inject_breathwork_target_missing():
    # Setup
    initial_content = "<html><body><p>No target here</p></body></html>"

    # Execute
    result = inject_breathwork(initial_content)

    # Verify
    # The content should remain unchanged since the target is not present
    assert result == initial_content
    assert new_section not in result
