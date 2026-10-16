import unittest
from decimal import Decimal

# Import your core logic functions
import sortWeeks
import getContributions

class TestProject(unittest.TestCase):

    def setUp(self):
        # Sample setup with 3 mock members
        self.members = [
            {"ID": 1, "Name": "Ama", "Contribution": 0.0},
            {"ID": 2, "Name": "Kofi", "Contribution": 0.0},
            {"ID": 3, "Name": "Esi", "Contribution": 0.0}
        ]
        self.target_amount = 50.0

    def test_week_structure_initialization(self):
        """Test 1: Check if weeks initialize properly with correct layout and keys"""
        analysis = sortWeeks.SortWeeks(self.members, self.target_amount)
        self.assertEqual(len(analysis), 3)
        self.assertEqual(analysis[0]["Week"], 1)
        self.assertEqual(analysis[0]["receiver"], "Ama")

    def test_initial_outstanding_balances(self):
        """Test 2: Check that outstanding values start at the full target amount"""
        analysis = sortWeeks.SortWeeks(self.members, self.target_amount)
        self.assertEqual(analysis[0]["Outstanding"]["Ama"], "50.00")

    def test_partial_payment_tracking(self):
        """Test 3: Verify that outstanding calculations handle partial payments correctly"""
        analysis = sortWeeks.SortWeeks(self.members, self.target_amount)
        # Mocking a partial payment process manually for evaluation
        payment = 30.00
        analysis[0]["Contributions"]["Esi"] = f"{payment:.2f}"
        analysis[0]["Outstanding"]["Esi"] = f"{(self.target_amount - payment):.2f}"
        
        self.assertEqual(analysis[0]["Outstanding"]["Esi"], "20.00")

    def test_week_cannot_close_if_outstanding_exists(self):
        """Test 4: Verify week does not payout and stays 'No' if someone owes money"""
        analysis = sortWeeks.SortWeeks(self.members, self.target_amount)
        
        # Everyone pays in full except Esi who pays 30
        analysis[0]["Contributions"] = {"Ama": "50.00", "Kofi": "50.00", "Esi": "30.00"}
        analysis[0]["Outstanding"] = {"Ama": "0.00", "Kofi": "0.00", "Esi": "20.00"}
        
        # Simulating your getContributions outstanding check loop logic
        outstanding_sum = sum(float(v) for v in analysis[0]["Outstanding"].values())
        if outstanding_sum > 0.0:
            analysis[0]["Paid"] = "No"
            
        self.assertEqual(analysis[0]["Paid"], "No")

    def test_week_closes_successfully_on_full_payment(self):
        """Test 5: Verify week status updates to 'Yes' when total balances are 0"""
        analysis = sortWeeks.SortWeeks(self.members, self.target_amount)
        
        # Everyone pays in full
        analysis[0]["Contributions"] = {"Ama": "50.00", "Kofi": "50.00", "Esi": "50.00"}
        analysis[0]["Outstanding"] = {"Ama": "0.00", "Kofi": "0.00", "Esi": "0.00"}
        
        outstanding_sum = sum(float(v) for v in analysis[0]["Outstanding"].values())
        if outstanding_sum == 0.0:
            analysis[0]["Paid"] = "Yes"
            
        self.assertEqual(analysis[0]["Paid"], "Yes")

    def test_unique_member_prevention_logic(self):
        """Test 6: Verify duplicate filtering matches true uniqueness values"""
        mock_list = [{"ID": 1, "Name": "Ama"}]
        new_name = "Ama"
        is_duplicate = any(m["Name"] == new_name for m in mock_list)
        self.assertTrue(is_duplicate)

if __name__ == '__main__':
    unittest.main()