import json
import sys
from color_rules import ColorCritic
from layout_rules import LayoutCritic

# Initialize Critics
color_critic = ColorCritic()
layout_critic = LayoutCritic()

def audit_visualization(chart_data):
    """
    Main tool function exposed to the AI.
    Input: JSON object with 'elements' (list of {text, color, bbox})
    """
    report = {
        "status": "PASS",
        "semantic_errors": [],
        "layout_errors": []
    }
    
    elements = chart_data.get('elements', [])
    
    # 1. Run Color Audit
    for elem in elements:
        text = elem.get('text', '')
        color = elem.get('color', '')
        if text and color:
            warning = color_critic.audit(text, color)
            if warning:
                report['semantic_errors'].append(warning)
                
    # 2. Run Layout Audit
    # Filter only elements with bounding boxes
    layout_elements = [e for e in elements if 'bbox' in e]
    layout_warnings = layout_critic.audit(layout_elements)
    report['layout_errors'].extend(layout_warnings)
    
    # Determine Final Status
    if report['semantic_errors'] or report['layout_errors']:
        report['status'] = "FAIL"
        
    return report

def main():
    """
    Simulates the MCP Server loop (Stdio).
    In a real implementation, this would use the 'mcp' library to handle JSON-RPC.
    """
    print("Viz Critic MCP Server Started...", file=sys.stderr)
    
    # Example of how it would process a request
    # (In reality, this comes from the AI via Stdin)
    sample_request = {
        "elements": [
            {"text": "Revenue Growth", "color": "red", "bbox": [10, 10, 100, 20]},
            {"text": "Profit", "color": "#006233", "bbox": [10, 35, 50, 15]},
            {"text": "Risk Warning", "color": "blue", "bbox": [12, 36, 80, 15]} # Overlaps Profit!
        ]
    }
    
    result = audit_visualization(sample_request)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
