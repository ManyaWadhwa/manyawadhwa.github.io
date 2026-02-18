"""
Python functions for data transformation.
These functions are loaded into Pyodide and can be called from JavaScript.

To add more functions:
1. Add your Python function here
2. It will be automatically loaded by index.html
3. Create a JavaScript wrapper function if needed
"""

# Dataset configuration: model -> prompt_type -> local JSONL path (relative to data-browser.html)
DATASET_CONFIG = {
    "GPT-4.1-mini": {
        "original": "data/GPT-4.1_model_name_gpt-4.1_variation_original.jsonl",
        "iterate":"data/GPT-4.1_model_name_gpt-4.1_variation_iterate.jsonl",
        # "creative": "connections-dev/res_gptoss20b_creative_1_None_0.7_4096_gpt-4_1-mini-2025-04-14"
    },
    "Gemini-3-Pro":{
        "original":"data/Gemini-3-pro_model_name_gemini-3-pro.jsonl",
    },
    "Olmo-3.1-32B-Think (32k)":{
        "original":"data/Olmo-3.1-32B-Think (32k)_model_name_allenai_Olmo-3.1-32B-Think.jsonl"
    }
}


def format_source_path(triple1_labels, triple2_labels, triple3_labels):
    """Format source path from triple labels"""
    import re
    parts = []
    if triple1_labels:
        # Remove single quotes and replace square brackets with round brackets
        str_val = str(triple1_labels).replace("'", "").replace("[", "(").replace("]", ")")
        # Add space after commas (but not if already present)
        parts.append(re.sub(r',(?!\s)', ', ', str_val))
    if triple2_labels:
        str_val = str(triple2_labels).replace("'", "").replace("[", "(").replace("]", ")")
        parts.append(re.sub(r',(?!\s)', ', ', str_val))
    if triple3_labels:
        str_val = str(triple3_labels).replace("'", "").replace("[", "(").replace("]", ")")
        parts.append(re.sub(r',(?!\s)', ', ', str_val))
    return " + ".join(parts)


def format_paths(paths_0):
    """Convert paths_0 array to list of lists. Handles both lists and numpy arrays."""
    if not paths_0:
        return []

    if isinstance(paths_0, str):
        import json
        paths_0 = json.loads(paths_0)
    
    # Convert numpy array to list if needed
    try:
        import numpy as np
        if isinstance(paths_0, np.ndarray):
            paths_0 = paths_0.tolist()
    except ImportError:
        pass  # numpy not available, assume it's already a list
    
    if isinstance(paths_0, list):
        result = []
        for path in paths_0:
            # Convert numpy array to list if needed
            try:
                import numpy as np
                if isinstance(path, np.ndarray):
                    path = path.tolist()
            except ImportError:
                pass
            
            if isinstance(path, list):
                result.append(path)
            else:
                result.append([path])
        return result
    else:
        return [[paths_0]]


def process_query(query):
    """Example: Process query text"""
    if not query:
        return "(empty)"
    return query.strip()


def filter_paths_by_length(paths, min_length=1, max_length=None):
    """Filter paths by length"""
    if not paths:
        return []
    
    filtered = []
    for path in paths:
        path_len = len(path) if isinstance(path, list) else 1
        if path_len >= min_length:
            if max_length is None or path_len <= max_length:
                filtered.append(path)
    return filtered


def extract_path_elements(paths, index=0):
    """Extract specific element from each path"""
    if not paths:
        return []
    
    result = []
    for path in paths:
        if isinstance(path, list) and len(path) > index:
            result.append(path[index])
        elif not isinstance(path, list) and index == 0:
            result.append(path)
    return result


def format_path_for_display(path):
    """
    Format a path structure into a list of triples for display.
    Handles various nested structures and flattens them.
    Supports both Python lists and numpy arrays.
    
    Args:
        path: Can be:
            - Deeply nested: [[[triple], [triple]], [[triple], [triple]]]
            - Nested triples: [[triple], [triple], [triple]]
            - Flat: [entity, relation, entity, relation, entity]
            - numpy.ndarray: Any of the above structures as numpy arrays
    
    Returns:
        List of triples, each triple is [entity, relation, entity]
    """
    if path is None:
        return []
    
    # Handle empty cases
    # try:
    #     if hasattr(path, '__len__') and len(path) == 0:
    #         return []
    # except:
    #     pass
    
    # Convert numpy array to list if needed
    try:
        import numpy as np
        if isinstance(path, np.ndarray):
            path = path.tolist()
    except ImportError:
        pass  # numpy not available, assume it's already a list
    except Exception:
        pass  # If conversion fails, try to continue
    
    all_triples = []
    
    # Recursively flatten nested structures
    def extract_triples(item):
        """Recursively extract triples from nested structures"""
        # Convert numpy array to list if needed
        try:
            import numpy as np
            if isinstance(item, np.ndarray):
                item = item.tolist()
        except ImportError:
            pass
        
        if item is None:
            return []
        
        if isinstance(item, list) or isinstance(item, np.ndarray):
            # Check if this is a triple (list with 2-3 elements)
            if len(item) >= 2:
                # Check if elements can be converted to strings (triples are usually strings)
                try:
                    # Try to convert first few elements to strings
                    test_elements = item[:min(3, len(item))]
                    # If we can convert them to strings, it's likely a triple
                    converted = [str(x) for x in test_elements]
                    if len(converted) >= 2:
                        return [converted]
                except (TypeError, ValueError):
                    pass
            
            # Otherwise, recurse into nested lists
            result = []
            for sub_item in item:
                try:
                    result.extend(extract_triples(sub_item))
                except Exception:
                    # Skip items that can't be processed
                    continue
            return result
        
        # If it's a single value, wrap it
        try:
            return [[str(item)]]
        except:
            return []
    
    # Use recursive extraction
    try:
        all_triples = extract_triples(path)
    except Exception as e:
        # If extraction fails, return empty list
        return []
    
    # Filter to ensure we only have valid triples (at least 2 elements)
    all_triples = [t for t in all_triples if isinstance(t, list) and len(t) >= 2]
    
    return all_triples


def process_paths_with_scores(instance):
    """
    Process paths with their corresponding scores from an instance and return structured data for table display.
    
    Args:
        instance: Dictionary containing the instance data with fields:
            - paths_0: List of paths
            - validity_per_path_0: List of validity scores (optional)
            - factualiy_scores_0: List of factuality scores (optional, alternate spelling)
            - factuality_scores_0: List of factuality scores (optional)
            - min_salience_scores_0: List of quality scores (optional)
    
    Returns:
        List of dictionaries, each containing:
        - path: List of triples, each triple is [entity, relation, entity]
        - formatted_path: Formatted string representation (for display)
        - valid: Validity score or None
        - factual: Factuality score or None
        - quality: Quality score or None
    """
    if not instance:
        return []
    
    # Extract data from instance
    paths_0 = instance.get('paths_0') or []
    validity_per_path_0 = instance.get('validity_per_path_0')
    factualiy_scores_0 = instance.get('factualiy_scores_0')
    factuality_scores_0 = instance.get('factuality_scores_0')
    min_salience_scores_0 = instance.get('min_salience_scores_0')

    # Handle paths_0 if it's a string (parse JSON)
    if isinstance(paths_0, str):
        import json
        try:
            paths_0 = json.loads(paths_0)
        except (json.JSONDecodeError, ValueError):
            # If JSON parsing fails, return empty list
            return []
    
    # Handle numpy arrays for paths_0
    try:
        import numpy as np
        if isinstance(paths_0, np.ndarray):
            paths_0 = paths_0.tolist()
    except ImportError:
        pass
    except Exception:
        pass
    
    if not paths_0:
        return []

    # Format paths (convert to list of lists)
    formatted_paths = format_paths(paths_0)
    
    # Use factuality_scores_0 if available, otherwise try factualiy_scores_0
    factual_scores = factuality_scores_0 if factuality_scores_0 is not None else factualiy_scores_0
    
    # Default to empty lists if None
    validity_scores = validity_per_path_0 or []
    factual_scores = factual_scores or []
    quality_scores = min_salience_scores_0 or []
    
    result = []
    for i, path in enumerate(formatted_paths):
        # Format the path into triples
        path_triples = format_path_for_display(path)
        
        # If no triples found, try to use the original path structure
        if not path_triples and path:
            # Fallback: try to use the path as-is if it's already in a usable format
            if isinstance(path, list) and len(path) > 0:
                # If path is already a list of lists (triples), use it directly
                if all(isinstance(item, list) and len(item) >= 2 for item in path):
                    path_triples = path
                # Otherwise, try one more time with the raw path
                else:
                    path_triples = format_path_for_display(path)
        
        entry = {
            'path': path_triples if path_triples else [],
            'valid': validity_scores[i] if i < len(validity_scores) else None,
            'factual': factual_scores[i] if i < len(factual_scores) else None,
            'quality': quality_scores[i] if i < len(quality_scores) else None
        }
        result.append(entry)
    
    return result


def preprocess_dataset(dataset):
    """
    Pre-process an entire dataset by adding processed_paths to each instance.
    
    Args:
        dataset: List of instance dictionaries
    
    Returns:
        List of instances with 'processed_paths' field added to each instance
    """
    if not dataset:
        return []
    
    processed_dataset = []
    for instance in dataset:
        # Create a copy of the instance
        processed_instance = dict(instance)
        # Add processed paths
        processed_instance['processed_paths'] = process_paths_with_scores(instance)
        processed_dataset.append(processed_instance)
    
    return processed_dataset


def get_dataset_config():
    """Get the dataset configuration dictionary"""
    return DATASET_CONFIG
