#!/bin/bash
# Simple wrapper for reproducible EAZY runs

DATE=$(date +%Y-%m-%d)
OUTDIR="outputs/run_${DATE}"

mkdir -p $OUTDIR

../src/eazy -p configs/zphot_jwst.param \
            -o $OUTDIR/photz \
            --allow-template-error

echo "EAZY run complete: results in $OUTDIR"