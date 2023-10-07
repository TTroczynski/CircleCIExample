import pytest
import model
import flask
from PIL import Image

def test_preprocess_img_given_IncorrectPath_FailsToProcess():
        with pytest.raises(Exception) as exceptionInfo:
                model.preprocess_img(" ")
        assert str(exceptionInfo.value) != "";

def test_load_Model_GivenNoPath_FailsToLoadModel():
        with pytest.raises(Exception) as ExceptionInfo:
                model.load_model(" ")
        assert str(ExceptionInfo.value) != "";


