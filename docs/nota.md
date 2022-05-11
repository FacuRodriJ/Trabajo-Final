<style type="text/css">
p {text-align: justify;}   
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-7btt{border-color:inherit;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:justify;vertical-align:top}
.tg .tg-1wig{border-color:inherit;font-weight:bold;text-align:justify;vertical-align:top}
</style>

# Planteo del problema

<p>Los establecimientos de canchas de fútbol que alquilan por hora en la ciudad de Posadas Misiones, tienen un principal problema y se trata de que no cuentan con una garantía en el caso de que un cliente reserve una cancha y no se presente. Este problema que mencionamos es bastante común en la mayoría de complejos de alquiler de canchas dado que para reservar se utiliza la vía telefónica, la mensajería tradicional y la mensajería instantánea de WhatsApp, Instagram, etc.
</p>

# Introducción y objetivos

<p>El proyecto que se presenta aquí será un Sistema de Gestión de Reservas para Complejos de Canchas, se tomará como referencia para la realización del análisis y requerimientos del proyecto al complejo Tercer Tiempo, pero a su vez se busca que todos los complejos que vean útil el sistema y quieran usarlo para sus establecimientos puedan hacerlo sin problemas.<br>
El principal objetivo del proyecto es la realización de un software que sustituya la utilización de la mensajería tradicional (SMS) y la mensajería instantánea (Instagram Direct Messenger, WhatsApp) por un sistema que permita realizar pagos, que ofrezca transparencia al propietario sobre el cliente, que reduzca las pérdidas de los complejos en caso de ausencia del cliente. 
</p>

# Alcance y limitaciones

<p>En esta versión del software se presentará un sistema que se ejecutará en navegadores web, no se contempla los sistemas Android y iOS para esta versión. Para futuras mejoras se plantea un módulo de calificaciones para emprendimientos y jugadores; un módulo que permita a cada establecimiento tener su propia tienda y permita a los jugadores elegir, por ejemplo, la pelota, bebidas post partido, entre otros; un chat en tiempo real para jugadores y establecimientos.
</p>

# Especificación de módulos

## Funcionales

<ul>
  <li> Reservas </li>
  <li> Pagos </li>
  <li> Asistencias </li>
  <li> Establecimientos </li>
  <li> Jugadores </li>
  <li> Estadística </li>
</ul>

## No funcionales

<ul>
  <li> Auditoría </li>
  <li> Seguridad de Datos </li>
  <li> Operatividad </li>
</ul>

# Descripción de los módulos

<p><b>Reservas:</b> se encarga de mostrar los horarios disponibles para reservas de cada establecimiento y todas las reservas registradas; permite a los jugadores elegir y reservar entre los horarios disponibles.
<br><br>
<b>Pagos:</b> registra y almacena cada uno de los pagos efectuados por los jugadores. El módulo brindará una plataforma de pagos online para que los jugadores paguen sus reservas directamente desde la web.
<br><br>
<b>Asistencias:</b> registra las asistencias e inasistencias de los jugadores que realizaron reservas previamente. Por cada reserva confirmada se genera un código QR que es enviado al jugador que realizó la reserva, el mismo debe ser escaneado en el establecimiento por la persona encargada.
<br><br>
<b>Establecimientos:</b> se encarga de registrar, almacenar, modificar y eliminar las cuentas de los establecimientos que se hayan registrado en el sistema, involucra las operaciones de CRUD (Create, Read, Update, Delete).
<br><br>
<b>Jugadores:</b> se encarga de registrar, almacenar, modificar y eliminar las cuentas de los jugadores que se hayan registrado en el sistema, involucra las operaciones de CRUD (Create, Read, Update, Delete).
<br><br>
<b>Estadística:</b> se encarga de calcular, generar y mostrar estadísticas con relación a los diferentes módulos en un periodo seleccionado por el usuario. Los resultados deberán desplegarse en gráficos y ser manipulables.
<br><br>
<b>Auditoría:</b> permite al administrador monitorear y tener constancia de los accesos de los usuarios a la información almacenada en la base de datos, incluyendo la creación, modificación y eliminación de datos.
<br><br>
<b>Seguridad de Datos:</b>
<ul>
  <li> Los permisos de acceso al sistema podrán ser cambiados solamente por el administrador de acceso a datos. </li>
  <li> Administrador: dispone de todas las prestaciones del sistema, sin restricciones. Tendrá a su disposición la creación de Usuarios y Roles de Usuario. El administrador elegirá los permisos de cada rol de usuario con respecto a los módulos. </li>
  <li> Ningún registro se eliminará de forma permanente de la base de datos por parte de los usuarios, en cambio se utilizará un borrado lógico. </li>
</ul>
<b>Operatividad:</b>
<ul>
  <li> El sistema se ejecutará en un navegador web. </li>
  <li> La aplicación web tendrá un diseño “Responsive”. </li>
  <li> El sistema deberá contar con manuales de usuario estructurados adecuadamente. </li>
  <li> El sistema deberá proporcionar mensajes de error que sean informativos y orientados al usuario final. </li>
  <li> El sistema poseerá interfaces gráficas simples y agradables al usuario. </li>
</ul>
</p>

# Procesos automatizados

<table class="tg">
<thead>
  <tr>
    <th class="tg-c3ow"><span style="font-weight:bold">**Denominación**</span></th>
    <th class="tg-c3ow"><span style="font-weight:bold">**Módulos que intervienen**</span></th>
    <th class="tg-c3ow"><span style="font-weight:bold">**Descripción del proceso**</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">Integración con la API de Mercado Pago</td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;
    background-color:transparent">Pagos</span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;
    background-color:transparent">Para este proceso se utilizará la Checkout API de Mercado Pago, esta permite crear una plataforma de pago, contando con la gestión de reembolsos y cancelaciones, entre otras funciones.</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none">Registro de Asistencias</span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;background-color:transparent">Asistencias, Jugadores</span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;
    background-color:transparent">Por cada reserva confirmada y pagada se le asignará y enviará, al jugador que realizó la reserva, un código QR. El mismo tendrá que ser escaneado en el establecimiento correspondiente.</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none">Avisos periódicos</span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;background-color:transparent">Reservas, Jugadores</span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;
    background-color:transparent">Se enviarán avisos periódicos a aquellos jugadores que hayan reservado un horario, el envió de avisos serán parametrizados por el propietario del establecimiento.</span></td>
  </tr>
</tbody>
</table>

# Estimación de tamaño por módulo

<table class="tg">
<thead>
  <tr>
    <th class="tg-7btt"><span style="font-weight:700;font-style:normal;text-decoration:none;background-color:transparent">Módulo</span></th>
    <th class="tg-7btt"><span style="font-weight:700;font-style:normal;text-decoration:none;background-color:transparent">Porcentaje de participación / Producto</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;
    background-color:transparent">Pagos</span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;
    background-color:transparent">30%</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;background-color:transparent">Reservas</span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;
    background-color:transparent">25%</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;background-color:transparent">Asistencias</span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;
    background-color:transparent">15%</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;background-color:transparent">Establecimientos</span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;
    background-color:transparent">10%</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;background-color:transparent">Jugadores</span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;
    background-color:transparent">10%</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;background-color:transparent">Auditoría</span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;
    background-color:transparent">5%</span></td>
  </tr>
  <tr>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;background-color:transparent">Estadísticas</span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;
    background-color:transparent">5%</span></td>
  </tr>
  <tr>
    <td class="tg-1wig"><span style="font-weight:700;font-style:normal;text-decoration:none;
    background-color:transparent">Total</span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;
    background-color:transparent">100%</span></td>
  </tr>
</tbody>
</table>

# Entorno tecnológico y metodológico

<table class="tg">
<thead>
  <tr>
    <th class="tg-1wig"><span style="font-weight:700;font-style:normal;text-decoration:none;background-color:transparent">Lenguajes de programación:</span></th>
    <th class="tg-1wig"><span style="font-weight:400;font-style:normal;text-decoration:none;background-color:transparent">Python, Javascript</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-1wig"><span style="font-weight:700;font-style:normal;text-decoration:none;background-color:transparent">Framework:</span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;background-color:transparent">Django</span></td>
  </tr>
  <tr>
    <td class="tg-1wig"><span style="font-weight:700;font-style:normal;text-decoration:none;background-color:transparent">Arquitectura:</span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;
    background-color:transparent">Modelo Vista Controlador</span></td>
  </tr>
  <tr>
    <td class="tg-1wig"><span style="font-weight:700;font-style:normal;text-decoration:none;
    background-color:transparent">Motor de Base de Datos:</span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;background-color:transparent">PostgreSQL</span></td>
  </tr>
  <tr>
    <td class="tg-1wig"><span style="font-weight:700;font-style:normal;text-decoration:none;background-color:transparent">Metodología seleccionada:</span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;
    background-color:transparent">UP (Proceso Unificado)</span></td>
  </tr>
  <tr>
    <td class="tg-1wig"><span style="font-weight:700;font-style:normal;text-decoration:none;
    background-color:transparent">Tipo de proyecto:</span></td>
    <td class="tg-0pky"><span style="font-weight:400;font-style:normal;text-decoration:none;
    background-color:transparent">Sin cliente final</span></td>
  </tr>
</tbody>
</table>

# Planificación de actividades

<table class="tg">
<thead>
  <tr>
    <th class="tg-7btt">Actividad</th>
    <th class="tg-7btt">Fecha de inicio</th>
    <th class="tg-7btt">Fecha de finalización</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">Modelado del Negocio</td>
    <td class="tg-c3ow">08/05/2022</td>
    <td class="tg-c3ow">05/06/2022</td>
  </tr>
  <tr>
    <td class="tg-0pky">Requerimientos</td>
    <td class="tg-c3ow">06/06/2022</td>
    <td class="tg-c3ow">20/06/2022</td>
  </tr>
  <tr>
    <td class="tg-0pky">Análisis Total del Sistema</td>
    <td class="tg-c3ow">21/06/2022</td>
    <td class="tg-c3ow">25/07/2022</td>
  </tr>
  <tr>
    <td class="tg-0pky">Correcciones necesarias de lo realizado</td>
    <td class="tg-c3ow">26/07/2022</td>
    <td class="tg-c3ow">01/08/2022</td>
  </tr>
  <tr>
    <td class="tg-0pky">Diseño 50% del sistema</td>
    <td class="tg-c3ow">02/08/2022</td>
    <td class="tg-c3ow">13/08/2022</td>
  </tr>
  <tr>
    <td class="tg-0pky">Codificación 50% del sistema</td>
    <td class="tg-c3ow">14/08/2022</td>
    <td class="tg-c3ow">25/08/2022</td>
  </tr>
  <tr>
    <td class="tg-0pky">Correcciones necesarias de lo realizado</td>
    <td class="tg-c3ow">26/08/2022</td>
    <td class="tg-c3ow">01/09/2022</td>
  </tr>
  <tr>
    <td class="tg-0pky">Diseño 75% del sistema</td>
    <td class="tg-c3ow">02/09/2022</td>
    <td class="tg-c3ow">13/09/2022</td>
  </tr>
  <tr>
    <td class="tg-0pky">Codificación 75% del sistema</td>
    <td class="tg-c3ow">14/09/2022</td>
    <td class="tg-c3ow">25/09/2022</td>
  </tr>
  <tr>
    <td class="tg-0pky">Correcciones necesarias de lo realizado</td>
    <td class="tg-c3ow">26/09/2022</td>
    <td class="tg-c3ow">01/10/2022</td>
  </tr>
  <tr>
    <td class="tg-0pky">Diseño 100% del sistema</td>
    <td class="tg-c3ow">02/10/2022</td>
    <td class="tg-c3ow">20/10/2022</td>
  </tr>
  <tr>
    <td class="tg-0pky">Codificación 100% del sistema</td>
    <td class="tg-c3ow">21/10/2022</td>
    <td class="tg-c3ow">15/11/2022</td>
  </tr>
  <tr>
    <td class="tg-0pky">Correcciones necesarias de lo realizado</td>
    <td class="tg-c3ow">16/11/2022</td>
    <td class="tg-c3ow">20/11/2022</td>
  </tr>
  <tr>
    <td class="tg-0pky">Pruebas</td>
    <td class="tg-c3ow">21/11/2022</td>
    <td class="tg-c3ow">10/12/2022</td>
  </tr>
</tbody>
</table>
