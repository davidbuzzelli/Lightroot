# Set environment variables
$env:OPENAI_API_KEY = "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"  # Insert your actual key here

# Set PYTHONPATH to current folder
$env:PYTHONPATH = (Get-Location).Path

# Launch the LightRoot CLI Co-Thinker
python examples\interactive_nomad.py
