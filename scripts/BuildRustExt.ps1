param($pyversion)

& conda create -n "build-py$pyversion" "python=$pyversion " --yes
Set-Location ../src/rust_extension
conda deactivate
& conda activate "build-py$pyversion "
maturin build -i python
conda deactivate

Set-Location ../../scripts