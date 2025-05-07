# Set PYTHONPATH to current folder
$env:PYTHONPATH = (Get-Location).Path

# Launch the LightRoot CLI Co-Thinker
python examples\interactive_nomad.py
