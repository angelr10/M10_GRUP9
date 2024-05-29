from odoo import models,fields, api

class Correo(models.Model):
    _name = 'angelcorreo03.correo'
    _description = 'Modelo de correo'

    email = fields.Char(string="direccion")
    opcion = fields.Integer(string="opcionElegida")
    nombreCliente = fields.Char(string="nombreCliente")
    #IDCliente
    tipoCorreo = fields.Selection(
        [
            ('reciennacidos','Recien Nacidos'),
            ('infantes','Infantes'),
            ('ninospequenos','Ninos pequeños'),
            ('ninos','Ninos'),
            ('preadolescentes','Pre Adolescentes')
        ],
        string="tipoCorreo" 
    )

    @api.model
    def obtenerTodo(self):
        #Obtiene una variable con todos los correos
        return self.search([])
        

class BusquedaCorreo(models.Model):
    _name = 'angelcorreo03.busquedacorreo'
    _description = 'Modelo de busquedaCorreo'

    tipoCorreo = fields.Selection(
        [
            ('reciennacidos','Recien Nacidos'),
            ('infantes','Infantes'),
            ('ninospequenos','Ninos pequeños'),
            ('ninos','Ninos'),
            ('preadolescentes','Pre Adolescentes')
        ],
        string="tipoCorreo" 
    )
    textoContenido = fields.Char(string="contenido del Correo")

    @api.model
    def send_email(self): #Se llama desde un boton
        correos = self.env['angelcorreo03.correo'].obtenerTodo()
        for correo in correos:
            template_id = self.env.ref('angelcorreo03.email_template_id').id
            email_values = {
                'email_to': correo.email,
                'body_html':self.textoContenido,
            }
            #self.env['mail.template'].browse(template_id).send_mail(self.id,email_values,force_send=True)