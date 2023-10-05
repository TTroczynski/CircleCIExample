import pytest
import model

def test_preprocess_img_given_IncorrectPath_FailsToProcess():
        with pytest.raises(Exception) as exceptionInfo:
                model.preprocess_img(" ")
        assert str(exceptionInfo.value) != "";
