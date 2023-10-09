"""Unit Tests"""
import pytest
import flask
import model

def test_preprocess_img_given_incorrect_path_throws_exception():
    """Validates exception thrown by preprocess_img when a path is improperly specified"""
    with pytest.raises(Exception) as exception_info:
        model.preprocess_img(" ")
    assert str(exception_info.value) != ""
def test_load_model_given_no_path_throws_exception():
    """Validates exception thrown by load_model is when a path is improperly specified"""
    with pytest.raises(Exception) as exception_info:
        model.load_model(" ")
    assert str(exception_info.value) != ""
def test_render_template_given_no_path_fails_to_load_template():
    """Validates exception thrown render_template when a path is improperly specified"""
    with pytest.raises(Exception) as exception_info:
        flask.render_template(" ")
    assert str(exception_info.value) != ""
def test_path_with_forward_brackets():
    """Validates exception thrown render_template when a path is improperly specified"""
    try:
        model.preprocess_img("test_images/0/Sign 0 (89).jpeg")
    except ValueError:
        pytest.fail("exception was thrown")
def test_path_with_backwards_brackets():
    """Validates exception thrown render_template when a path is improperly specified"""
    try:
        model.preprocess_img("test_images\\0\\Sign 0 (89).jpeg")
    except ValueError:
        pytest.fail("exception was thrown")
        