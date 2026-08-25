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
