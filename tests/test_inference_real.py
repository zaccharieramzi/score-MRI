from unittest.mock import patch

from score_mri.inference_real import main


def test_inference_real():
    args = [
        "main",
        "--task", "retrospective",
        "--data", "001",
        "--mask_type", "gaussian1d",
        "--acc_factor", "4",
        "--center_fraction", "0.08",
        "--N", "2",
    ]
    with patch("sys.argv", args):
        main()
