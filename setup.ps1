# Workshop Setup Script
# This script creates directory junctions to the Workshop_EdgeAI submodule

Write-Host "Setting up workshop directory junctions..." -ForegroundColor Cyan

# Ensure we're in the script directory
Set-Location $PSScriptRoot

# Check if lib/Workshop_EdgeAI exists
if (-not (Test-Path "lib\Workshop_EdgeAI")) {
    Write-Host "Error: lib\Workshop_EdgeAI not found. Please run 'git submodule update --init --recursive' first." -ForegroundColor Red
    exit 1
}

# Create junctions for each workshop folder
$workshops = @("3.1", "3.2", "5.1", "5.4")

foreach ($workshop in $workshops) {
    # Remove existing junction/directory if it exists
    if (Test-Path $workshop) {
        Write-Host "Removing existing $workshop..." -ForegroundColor Yellow
        cmd /c rmdir $workshop 2>$null
        Remove-Item $workshop -Force -Recurse -ErrorAction SilentlyContinue
    }
    
    # Create the junction
    $target = "lib\Workshop_EdgeAI\$workshop"
    if (Test-Path $target) {
        Write-Host "Creating junction: $workshop -> $target" -ForegroundColor Green
        cmd /c mklink /J $workshop $target | Out-Null
        if ($LASTEXITCODE -eq 0) {
            Write-Host "[OK] Successfully created $workshop" -ForegroundColor Green
        } else {
            Write-Host "[FAIL] Failed to create $workshop" -ForegroundColor Red
        }
    } else {
        Write-Host "[WARNING] $target does not exist, skipping" -ForegroundColor Yellow
    }
}

Write-Host "`nSetup complete!" -ForegroundColor Cyan
Write-Host "The workshop folders (3.1, 3.2, 5.1, 5.4) are now linked to lib/Workshop_EdgeAI" -ForegroundColor White
