# Introducción a Vue 3

Las _slides_ del curso están bastante bien y están [aquí](https://github.com/sdras/intro-to-vue).

Los ejercicios del curso están resueltos en [Codepen](https://codepen.io/your-work). Los que utilizan `vue-cli` están en este directorio.

Notas sobre el curso de Front End Masters [Introduction to Vue 3](https://frontendmasters.com/courses/vue-3/)

- **Es declarativo, no imperativo**. No dictamos lo que sucede de manera literal. El trabajo duro se le deja al sistema.
- **Controlamos mejor el estado** sin hacer llamadas al DOM
- Es **legible**. Se puede distinguir facilmente entre métodos, computadas, watchers...
- Es **fácil de mantener**: simple y fácil de aprender
- **Poderoso**: simple en apariencia pero te deja indagar en su complejida
- Tiene **cosas prestadas** que funcionan bien de otros frameworks
- **Elegante**
- **Evita la complejidad** de muchas tareas gracias a su diseño
- Se puede  **avanzar el proyecto**  hacia el siguiente hito sin que sea necesario desarrollar funciones complejas, pero necesarias. _Keeps from Yak shaving_


# Comparando Vue con otros _frameworks_

- Ofrece un D**OM virtual** como React o Angular y otros
- Ofrece **componentes reactivos** en la capa de la vista solo (similar pero diferente a React y Angular), React no es reactive. Se puede hacer reactivo con el uso de librerías, pero solo en la capa de la vista. Angular es Reactive, pero es MVC. Ofrece reactividad en el modelo, vista y controladores.
- Tiene props y un **manejo del estado centralizado** como React
- Tiene **renderizado condicional**, similar a Angular 
- La **simplicidad y la performance** esta inspirada de Polymer. Los _single file components_, un fichero con una sección para HTML, estilos (y javascript) 
- El **atributo scope** sobre los estilos hace que los estilos se apliquen solo sobre ese componente en concreto. React tiene módulos CSS como CSS-in-JS que funcionan similar 
