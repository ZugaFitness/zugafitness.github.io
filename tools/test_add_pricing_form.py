import unittest
from add_pricing_form import add_pricing_form_to_html, pricing_and_form_html

class TestAddPricingForm(unittest.TestCase):
    def test_add_pricing_form_to_html_match(self):
        # Setup: HTML content that matches the regex
        original_content = (
            "<p><strong>Takeaway:</strong> Corporate Zumba is a fun, high-energy cardio "
            "workout that doubles as an effective team-building activity.</p>\n"
            "  </div>\n"
            "</div>"
        )

        # Action: call the function
        result = add_pricing_form_to_html(original_content)

        # Verification: ensure the result contains the form html right after the match
        expected_content = original_content + "\n" + pricing_and_form_html
        self.assertEqual(result, expected_content)
        self.assertIn("Transparent B2B Pricing", result)
        self.assertIn("Book Your Corporate Wellness Session", result)

    def test_add_pricing_form_to_html_no_match(self):
        # Setup: HTML content that does not match the regex exactly
        original_content = (
            "<p><strong>Takeaway:</strong> Corporate Zumba is a fun activity.</p>\n"
            "  </div>\n"
            "</div>"
        )

        # Action: call the function
        result = add_pricing_form_to_html(original_content)

        # Verification: the content should remain unchanged
        self.assertEqual(result, original_content)
        self.assertNotIn("Transparent B2B Pricing", result)

if __name__ == '__main__':
    unittest.main()
import pytest
from add_pricing_form import insert_pricing_form, pricing_and_form_html

def test_insert_pricing_form_success():
    """Test that the pricing form is correctly inserted when the target string is present."""
    mock_html = '''
<div class="row">
  <div class="col-md-6">
    <p><strong>Takeaway:</strong> Corporate Zumba is a fun, high-energy cardio workout that doubles as an effective team-building activity.</p>
  </div>
</div>
'''

    expected_html = f'''
<div class="row">
  <div class="col-md-6">
    <p><strong>Takeaway:</strong> Corporate Zumba is a fun, high-energy cardio workout that doubles as an effective team-building activity.</p>
  </div>
</div>
{pricing_and_form_html}
'''

    result = insert_pricing_form(mock_html)
    assert result.strip() == expected_html.strip()
    assert pricing_and_form_html in result

def test_insert_pricing_form_missing_target():
    """Test that the HTML remains unchanged if the target string is not found."""
    mock_html = '''
<div class="row">
  <div class="col-md-6">
    <p>Some other content</p>
  </div>
</div>
'''
    result = insert_pricing_form(mock_html)
    assert result == mock_html
    assert pricing_and_form_html not in result
