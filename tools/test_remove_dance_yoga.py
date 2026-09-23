import unittest
from remove_dance_yoga import remove_dance_card

class TestRemoveDanceYoga(unittest.TestCase):

    def test_remove_dance_card_middle_of_list(self):
        """Test removing the card when it's between other elements (has a following comment)."""
        html_content = """
        <div class="row">
            <!-- First Plan -->
            <div class="col-md-3 mb-4">
                Plan 1
            </div>
            <!-- Starter Dance -->
            <div class="col-md-3 mb-4">
                <div class="card h-100 shadow-sm border-0">
                    Starter Dance Content
                </div>
            </div>
            <!-- Growth Plan -->
            <div class="col-md-3 mb-4">
                Plan 2
            </div>
        </div>
        """

        expected_content = """
        <div class="row">
            <!-- First Plan -->
            <div class="col-md-3 mb-4">
                Plan 1
            </div>
            <!-- Growth Plan -->
            <div class="col-md-3 mb-4">
                Plan 2
            </div>
        </div>
        """

        result = remove_dance_card(html_content)
        # Strip blank lines for comparison as spacing might differ slightly
        self.assertEqual(
            "\n".join([line for line in result.split("\n") if line.strip()]),
            "\n".join([line for line in expected_content.split("\n") if line.strip()])
        )

    def test_remove_dance_card_end_of_list(self):
        """Test removing the card when it's the last element (no following comment)."""
        html_content = """
        <div class="row">
            <!-- First Plan -->
            <div class="col-md-3 mb-4">
                Plan 1
            </div>
            <!-- Starter Dance -->
            <div class="col-md-3 mb-4">
                <div class="card">Starter Dance Content</div>
            </div>
        </div>
        """

        expected_content = """
        <div class="row">
            <!-- First Plan -->
            <div class="col-md-3 mb-4">
                Plan 1
            </div>
        </div>
        """

        result = remove_dance_card(html_content)
        self.assertEqual(
            "\n".join([line for line in result.split("\n") if line.strip()]),
            "\n".join([line for line in expected_content.split("\n") if line.strip()])
        )

    def test_remove_dance_card_not_present(self):
        """Test that nothing changes if the Starter Dance card is not present."""
        html_content = """
        <div class="row">
            <!-- First Plan -->
            <div class="col-md-3 mb-4">
                Plan 1
            </div>
            <!-- Growth Plan -->
            <div class="col-md-3 mb-4">
                Plan 2
            </div>
        </div>
        """

        result = remove_dance_card(html_content)
        self.assertEqual(result.strip(), html_content.strip())

    def test_remove_dance_card_different_spacing(self):
        """Test with different spacing around the comment tags."""
        html_content = """
        <div class="row">
            <!--Starter Dance-->
            <div class="col-md-3 mb-4">
                <div class="card h-100 shadow-sm border-0">
                    Starter Dance Content
                </div>
            </div>
            <!-- Growth Plan -->
        """

        expected_content = """
        <div class="row">
            <!-- Growth Plan -->
        """

        result = remove_dance_card(html_content)
        self.assertEqual(
            "\n".join([line for line in result.split("\n") if line.strip()]),
            "\n".join([line for line in expected_content.split("\n") if line.strip()])
        )

if __name__ == '__main__':
    unittest.main()
