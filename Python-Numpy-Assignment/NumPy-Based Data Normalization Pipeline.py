import numpy

def normalization_pipeline(data: numpy.ndarray):
    # Calculate statistics
    mean = numpy.mean(data)
    std = numpy.std(data)
    
    # Perform Z-score normalization
    normalized = (data - mean) / std
    
    # Determine reshape dimensions (aiming for near-square)
    size = data.size
    rows = int(numpy.sqrt(size))
    cols = size // rows
    
    # Reshape the normalized data
    reshaped = normalized[:rows * cols].reshape(rows, cols)
    
    return normalized, reshaped

if __name__ == "__main__":
    # Input data
    data = numpy.array([10, 20, 30, 40])
    
    # Get results from pipeline
    normalized, reshaped = normalization_pipeline(data)
    
    # Output formatting
    print(f"original data: {data}")
    print(f"mean: {numpy.mean(data)}")
    print(f"standard deviation: {numpy.std(data):.2f}")
    print(f"normalized data: {normalized}")
    print(f"reshaped data shape: {reshaped.shape}")
    print(f"reshaped data:\n{reshaped}")
