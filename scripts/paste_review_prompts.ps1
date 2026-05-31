param(
    [string] $RunId = "web-research-test",
    [int] $Round = 1,
    [int] $DelaySeconds = 7,
    [switch] $Submit
)

$ErrorActionPreference = "Stop"

function Get-RoundName([int] $RoundNumber) {
    return "round_{0:D3}" -f $RoundNumber
}

$RoundName = Get-RoundName $Round
$Base = "rounds\$RunId\$RoundName\prompts"
$GptPrompt = "$Base\gpt_pro_thinking_review.md"
$GeminiPrompt = "$Base\gemini_deep_think_review.md"

Write-Host ""
Write-Host "Step 1/2: ChatGPT Extended Pro review prompt"
Write-Host "Focus the ChatGPT input box before the countdown ends."
$GptArgs = @(
    "-NoProfile",
    "-ExecutionPolicy", "Bypass",
    "-File", "scripts\paste_web_prompt.ps1",
    "-PromptPath", $GptPrompt,
    "-DelaySeconds", $DelaySeconds
)
if ($Submit) {
    $GptArgs += "-Submit"
}
& powershell @GptArgs

Write-Host ""
Write-Host "Step 2/2: Gemini Pro Deep Think review prompt"
Write-Host "Focus the Gemini input box before the countdown ends."
$GeminiArgs = @(
    "-NoProfile",
    "-ExecutionPolicy", "Bypass",
    "-File", "scripts\paste_web_prompt.ps1",
    "-PromptPath", $GeminiPrompt,
    "-DelaySeconds", $DelaySeconds
)
if ($Submit) {
    $GeminiArgs += "-Submit"
}
& powershell @GeminiArgs

Write-Host ""
Write-Host "After both models finish, use Copy response and save to:"
Write-Host "  handoff\$RunId\$RoundName\reviews\gpt_pro_thinking.md"
Write-Host "  handoff\$RunId\$RoundName\reviews\gemini_deep_think.md"
