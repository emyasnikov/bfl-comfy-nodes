from .bfl_api import (
    FluxPro,
    FluxDev,
    FluxPro11,
    FluxCanny,
    FluxDepth,
    FluxUltra11,
    FluxProFill,
    FluxProFinetune,
    FluxProCannyFinetune,
    FluxProDepthFinetune,
    FluxProFillFinetune,
    FluxUltra11Finetune,
)

NODE_CLASS_MAPPINGS = {
    "FLUX 1.0 [pro]": FluxPro,
    "FLUX 1.0 [dev]": FluxDev,
    "FLUX 1.1 [pro]": FluxPro11,
    "FLUX 1.1 [ultra]": FluxUltra11,
    "FLUX 1.0 [depth]": FluxDepth,
    "FLUX 1.0 [canny]": FluxCanny,
    "FLUX 1.0 [fill]": FluxProFill,
    "FLUX 1.0 [pro] Finetuned": FluxProFinetune,
    "FLUX 1.0 [canny] Finetuned": FluxProCannyFinetune,
    "FLUX 1.0 [depth] Finetuned": FluxProDepthFinetune,
    "FLUX 1.0 [fill] Finetuned": FluxProFillFinetune,
    "FLUX 1.1 [ultra] Finetuned": FluxUltra11Finetune,
}
