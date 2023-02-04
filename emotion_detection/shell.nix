{ pkgs ? import <nixpkgs> { config.allowUnfree = true; config.cudaSupport = true; } }:

pkgs.mkShell rec{

  nativeBuildInputs = with pkgs; [
    python39
    python39Packages.flask
    python39Packages.tensorflow
    python39Packages.pytorch
    python39Packages.gunicorn
    python39Packages.packaging
    python39Packages.keras
  ];

  buildInputs = [ pkgs.docker];

  venvDir = "./.venv";

  shellHook = ''
    set -h #remove "bash: hash: hashing disabled" warning !
    SOURCE_DATE_EPOCH=$(date +%s)
    if ! [ -d "${venvDir}" ]; then
      python -m venv "${venvDir}"
    fi
    source "${venvDir}/bin/activate"

  '';
}

