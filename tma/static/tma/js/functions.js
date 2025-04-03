function confirmDelete(event) {
    if (!confirm("¿Estás seguro de que quieres eliminar este evento?")) {
        event.preventDefault();  // Evita que el formulario se envíe
        return false;
    }
    return true;
}