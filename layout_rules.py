class LayoutCritic:
    """
    Enforces layout rules: Collision detection and spacing.
    """
    
    @staticmethod
    def check_intersection(box_a, box_b):
        """
        Checks if two bounding boxes intersect.
        Box format: (x, y, width, height)
        """
        x1, y1, w1, h1 = box_a
        x2, y2, w2, h2 = box_b
        
        # Calculate edges
        l1, r1, t1, b1 = x1, x1 + w1, y1, y1 + h1
        l2, r2, t2, b2 = x2, x2 + w2, y2, y2 + h2
        
        # Check for non-overlap
        if r1 < l2 or r2 < l1 or b1 < t2 or b2 < t1:
            return False # No overlap
        return True # Overlap detected

    def audit(self, text_elements):
        """
        Audits a list of text elements for collisions.
        Input: List of dicts {'text': str, 'bbox': (x, y, w, h)}
        """
        errors = []
        
        for i in range(len(text_elements)):
            for j in range(i + 1, len(text_elements)):
                elem_a = text_elements[i]
                elem_b = text_elements[j]
                
                if self.check_intersection(elem_a['bbox'], elem_b['bbox']):
                    errors.append(
                        f"⚠️ Layout Error: Text '{elem_a['text']}' overlaps with '{elem_b['text']}'."
                    )
                    
        return errors

# Test the logic
if __name__ == "__main__":
    critic = LayoutCritic()
    
    # Simulated text elements (x, y, w, h)
    elements = [
        {'text': 'Title', 'bbox': (10, 10, 100, 20)},
        {'text': 'Subtitle', 'bbox': (10, 35, 80, 15)},  # Safe (below title)
        {'text': 'Label A', 'bbox': (50, 100, 30, 10)},
        {'text': 'Label B', 'bbox': (60, 105, 30, 10)}   # Overlaps Label A!
    ]
    
    print("--- Running Layout Audit ---")
    results = critic.audit(elements)
    if results:
        for err in results:
            print(f"[FAIL] {err}")
    else:
        print("[PASS] No layout collisions found.")
