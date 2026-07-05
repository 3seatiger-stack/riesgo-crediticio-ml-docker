# Uso responsable de herramientas de IA para documentación

## Propósito

Durante la preparación técnica se pueden utilizar asistentes como GitHub Copilot o herramientas de IA generativa para apoyar:

- generación inicial de docstrings;
- revisión de claridad del README;
- propuestas de casos de prueba;
- explicación de comandos;
- detección de inconsistencias documentales.

## Criterio de uso

La herramienta de IA se considera apoyo, no fuente automática de verdad. Toda sugerencia debe:

1. revisarse manualmente;
2. probarse en el entorno real;
3. contrastarse con el comportamiento del código;
4. evitar inclusión de secretos;
5. documentarse cuando sea relevante para la trazabilidad académica.

## Ejemplo de uso de Copilot

Prompt sugerido:

```text
Revisa este endpoint FastAPI y propone una docstring técnica que describa
entrada, salida, errores esperados y comportamiento del umbral, sin modificar
la lógica del código.
```

## Validación humana

La documentación final debe corresponder con:

- nombres reales de endpoints;
- variables reales;
- comandos realmente ejecutados;
- versiones del repositorio;
- resultados observados.

## Declaración

En esta entrega, la IA se utiliza como herramienta de apoyo para acelerar estructuración y revisión. La responsabilidad sobre la exactitud técnica, pruebas y conclusiones permanece en el autor.
