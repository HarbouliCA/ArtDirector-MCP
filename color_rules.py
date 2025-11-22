import re

class ColorCritic:
    """
    Enforces semantic color rules for data visualizations.
    """
    
    # Semantic Keywords
    RED_KEYWORDS = [r'danger', r'decrease', r'loss', r'error', r'churn', r'deficit', r'drop', r'negative', r'missed', r'cost', r'expense', r'spending']
    GREEN_KEYWORDS = [r'safe', r'increase', r'profit', r'success', r'win', r'revenue', r'growth', r'positive', r'scored', r'goal']
    ORANGE_KEYWORDS = [r'risk', r'warning', r'potential', r'pending', r'review', r'caution']

    # Standard Hex Codes (Simplified for matching)
    # In a real app, we would use color distance algorithms
    RED_HEX = ['#FF0000', '#CC0000', '#8B0000', 'red', 'darkred']
    GREEN_HEX = ['#00FF00', '#008000', '#006400', 'green', 'darkgreen', '#006233'] # Added Morocco Green
    ORANGE_HEX = ['#FFA500', '#FF8C00', '#FF4500', 'orange', 'darkorange']

    @staticmethod
    def is_color_match(color, target_colors):
        """Checks if a color string matches a target set (simple string match for now)."""
        return color.lower() in [c.lower() for c in target_colors]

    def audit(self, label, color):
        """
        Audits a single Label/Color pair.
        Returns a warning string if a violation is found, else None.
        """
        label_lower = label.lower()
        
        # 1. Check RED Rules
        for keyword in self.RED_KEYWORDS:
            if re.search(keyword, label_lower):
                if not self.is_color_match(color, self.RED_HEX):
                    return f"⚠️ Semantic Error: '{label}' implies Negative/Danger but is colored '{color}'. Suggest using RED."

        # 2. Check GREEN Rules
        for keyword in self.GREEN_KEYWORDS:
            if re.search(keyword, label_lower):
                if not self.is_color_match(color, self.GREEN_HEX):
                    return f"⚠️ Semantic Error: '{label}' implies Positive/Growth but is colored '{color}'. Suggest using GREEN."

        # 3. Check ORANGE Rules
        for keyword in self.ORANGE_KEYWORDS:
            if re.search(keyword, label_lower):
                if not self.is_color_match(color, self.ORANGE_HEX):
                    return f"⚠️ Semantic Error: '{label}' implies Risk/Warning but is colored '{color}'. Suggest using ORANGE."

        return None # No violations

# Test the logic
if __name__ == "__main__":
    critic = ColorCritic()
    
    test_cases = [
        ("Revenue Growth", "red"),      # Should Fail
        ("Churn Rate", "green"),        # Should Fail
        ("Potential Risk", "blue"),     # Should Fail
        ("Profit", "#006233"),          # Should Pass (Morocco Green)
        ("Server Error", "red")         # Should Pass
    ]
    
    print("--- Running Color Audit ---")
    for label, color in test_cases:
        result = critic.audit(label, color)
        if result:
            print(f"[FAIL] {result}")
        else:
            print(f"[PASS] '{label}' is correctly colored.")
