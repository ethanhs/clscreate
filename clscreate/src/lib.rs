use pyo3::prelude::*;

#[pyclass]
pub struct Example {
    #[pyo3(get, set)]
    pub a: i64,
    #[pyo3(get, set)]
    pub b: String,
}

#[pymethods]
impl Example {
    #[new]
    fn new() -> Self {
        Example {
            a: 4,
            b: String::from("Hello"),
        }
    }
}

#[pymodule]
fn clscreate_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Example>()?;
    Ok(())
}
