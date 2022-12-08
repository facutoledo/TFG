from django.test import TestCase
from django.contrib.auth import get_user_model


class TestCuentaDeUsuario(TestCase):
    def test_nuevo_administrador(self):
        db = get_user_model()
        administrador = db.objects.create_superuser(
            "1", "correo_electronico@a.com", "password")
        self.assertEqual(administrador.dni, "1")
        self.assertEqual(administrador.correo_electronico, "correo_electronico@a.com")
        self.assertTrue(administrador.is_superuser)
        self.assertTrue(administrador.is_staff)
        self.assertTrue(administrador.is_active)
        self.assertTrue(administrador.es_medico)
        self.assertTrue(administrador.es_paciente)
        self.assertEqual(str(administrador), "1")

        with self.assertRaises(ValueError):
            db.objects.create_superuser(dni="2", correo_electronico="correo_electronico@a.com", password="password", is_superuser=False)
        
        with self.assertRaises(ValueError):
            db.objects.create_superuser(dni="3", correo_electronico="correo_electronico@a.com", password="password", is_staff=False)
        
        with self.assertRaises(ValueError):
            db.objects.create_superuser(dni="4", correo_electronico="correo_electronico@a.com", password="password", is_active=False)
        
        with self.assertRaises(ValueError):
            db.objects.create_superuser(dni="5", correo_electronico="correo_electronico@a.com", password="password", es_medico=False)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(dni="6", correo_electronico="correo_electronico@a.com", password="password", es_paciente=False)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(dni='', correo_electronico="correo_electronico@a.com", password="password")

        with self.assertRaises(ValueError):
            db.objects.create_superuser(dni="7", correo_electronico="", password="password")

    def test_nuevo_usuario(self):
        db = get_user_model()
        usuario = db.objects.create_user(
            "9", "correo_electronico@a.com", "password")
        self.assertEqual(usuario.dni, "9")
        self.assertEqual(usuario.correo_electronico, "correo_electronico@a.com")
        self.assertFalse(usuario.is_staff)
        self.assertFalse(usuario.is_superuser)

        self.assertFalse(usuario.is_active)
        self.assertFalse(usuario.es_medico)
        self.assertFalse(usuario.es_paciente)
        self.assertEqual(str(usuario), "9")

        with self.assertRaises(ValueError):
            db.objects.create_user(dni='', correo_electronico="correo_electronico@a.com", password="password")

        with self.assertRaises(ValueError):
            db.objects.create_user(dni="10", correo_electronico="", password="password")

    def test_nuevo_personal(self):
        db = get_user_model()
        usuario = db.objects.create_personal(
            "11", "correo_electronico@a.com", "password")
        self.assertEqual(usuario.dni, "11")
        self.assertEqual(usuario.correo_electronico, "correo_electronico@a.com")
        self.assertFalse(usuario.is_superuser)
        self.assertTrue(usuario.is_staff)
        self.assertFalse(usuario.is_active)
        self.assertFalse(usuario.es_medico)
        self.assertFalse(usuario.es_paciente)
        self.assertEqual(str(usuario), "11")

        with self.assertRaises(ValueError):
            db.objects.create_personal(dni='', correo_electronico="correo_electronico@a.com", password="password")

        with self.assertRaises(ValueError):
            db.objects.create_personal(dni="12", correo_electronico="", password="password")
        
    def test_nuevo_medico(self):
        db = get_user_model()
        usuario = db.objects.create_medico(
            "13", "correo_electronico@a.com", "password")
        self.assertEqual(usuario.dni, "13")
        self.assertEqual(usuario.correo_electronico, "correo_electronico@a.com")
        self.assertFalse(usuario.is_superuser)
        self.assertTrue(usuario.is_staff)
        self.assertFalse(usuario.is_active)
        self.assertTrue(usuario.es_medico)
        self.assertFalse(usuario.es_paciente)
        self.assertEqual(str(usuario), "13")

        with self.assertRaises(ValueError):
            db.objects.create_medico(dni='', correo_electronico="correo_electronico@a.com", password="password")

        with self.assertRaises(ValueError):
            db.objects.create_medico(dni="14", correo_electronico="", password="password")

    def test_nuevo_paciente(self):
        db = get_user_model()
        usuario = db.objects.create_paciente(
            "15", "correo_electronico@a.com", "password")
        self.assertEqual(usuario.dni, "15")
        self.assertEqual(usuario.correo_electronico, "correo_electronico@a.com")
        self.assertFalse(usuario.is_superuser)
        self.assertFalse(usuario.is_staff)
        self.assertFalse(usuario.is_active)
        self.assertFalse(usuario.es_medico)
        self.assertTrue(usuario.es_paciente)
        self.assertEqual(str(usuario), "15")

        with self.assertRaises(ValueError):
            db.objects.create_paciente(dni='', correo_electronico="correo_electronico@a.com", password="password")

        with self.assertRaises(ValueError):
            db.objects.create_paciente(dni="16", correo_electronico="", password="password")