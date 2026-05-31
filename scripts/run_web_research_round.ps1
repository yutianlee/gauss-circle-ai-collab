param(
    [string] $RunId = "web-research-test",
    [int] $Round = 1
)

$ErrorActionPreference = "Stop"

$Python = "C:\Users\yutia\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
if (-not (Test-Path -LiteralPath $Python)) {
    $Python = "python"
}

& $Python -m math_collab.orchestrator `
    --config config/agents.web-test.json `
    --problem problems/gauss_circle.md `
    --run-id $RunId `
    --start-round $Round `
    --rounds 1

Write-Host ""
Write-Host "Next:"
Write-Host "1. Open prompt files under rounds/$RunId/round_$($Round.ToString('000'))/prompts."
Write-Host "   Prompt filenames include the round suffix, e.g. *_$Round.md."
Write-Host "2. Paste them into ChatGPT Extended Pro and Gemini Pro Deep Think."
Write-Host "3. Use Copy response and save Markdown under handoff/$RunId/round_$($Round.ToString('000'))."
Write-Host "4. Rerun this script for the same round until judge completes, then increment -Round."
