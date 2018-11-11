#!/bin/bash
set -ue

usage () {
  echo "Usage: $0 {ultraauth|github}"
  exit
}

[[ $# -eq 1 ]] || usage

source "$1.env"
jupyterhub -f "jupyterhub_config_${1}.py"
