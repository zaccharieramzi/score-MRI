from unittest.mock import patch

from score_mri.inference_multi_coil_SSOS import main


def test_inference_multi_coil_SSOS():
    args = [
        "main",
        "--data", "001",
        "--mask_type", "gaussian1d",
        "--acc_factor", "4",
        "--center_fraction", "0.08",
        "--N", "2",
    ]
    with patch("sys.argv", args):
        main()
